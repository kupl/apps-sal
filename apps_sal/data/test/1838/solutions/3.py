def get_relation(synonyms, antonyms, word1, word2):
    if word1 not in synonyms or word2 not in synonyms:
        return '3'
    group1 = synonyms[word1]
    group2 = synonyms[word2]
    if group1 == group2:
        return '1'
    if group1 in antonyms and antonyms[group1] == group2:
        return '2'
    return '3'


def unify_synonyms(synonyms, groups, group1, group2):
    min_group = min(group1, group2)
    max_group = max(group1, group2)
    max_synonyms = groups[max_group]
    for synonym in max_synonyms:
        synonyms[synonym] = min_group
    update_groups(groups, min_group, max_synonyms)
    return (min_group, max_group)


def make_synonyms(synonyms, antonyms, groups, group1, group2):
    (min_group1, max_group1) = unify_synonyms(synonyms, groups, group1, group2)
    if group1 in antonyms and group2 in antonyms:
        (min_group2, max_group2) = unify_synonyms(synonyms, groups, antonyms[group1], antonyms[group2])
        del antonyms[min_group1]
        del antonyms[max_group1]
        del antonyms[min_group2]
        del antonyms[max_group2]
        antonyms[min_group1] = min_group2
        antonyms[min_group2] = min_group1
        return min_group1
    if max_group1 in antonyms:
        antonym_group = antonyms[max_group1]
        del antonyms[max_group1]
        antonyms[min_group1] = antonym_group
        antonyms[antonym_group] = min_group1
    return min_group1


def update_groups(groups, group, words):
    if group in groups:
        groups[group].update(words)
    else:
        groups.update({group: set(words)})


def make_relation(synonyms, antonyms, groups, word1, word2, relation, current_group):
    if relation == '1':
        if word1 not in synonyms and word2 not in synonyms:
            current_group += 1
            synonyms[word1] = current_group
            synonyms[word2] = current_group
            update_groups(groups, current_group, [word1, word2])
            return current_group
        if word1 not in synonyms:
            synonyms[word1] = synonyms[word2]
            update_groups(groups, synonyms[word2], [word1])
            return current_group
        if word2 not in synonyms:
            synonyms[word2] = synonyms[word1]
            update_groups(groups, synonyms[word1], [word2])
            return current_group
        group1 = synonyms[word1]
        group2 = synonyms[word2]
        if group1 != group2:
            make_synonyms(synonyms, antonyms, groups, group1, group2)
        return current_group
    if relation == '2':
        if word1 not in synonyms:
            current_group += 1
            group1 = current_group
            synonyms[word1] = group1
            update_groups(groups, group1, [word1])
        else:
            group1 = synonyms[word1]
        if word2 not in synonyms:
            current_group += 1
            group2 = current_group
            synonyms[word2] = group2
            update_groups(groups, group2, [word2])
        else:
            group2 = synonyms[word2]
        if group1 not in antonyms and group2 not in antonyms:
            antonyms[group1] = group2
            antonyms[group2] = group1
            return current_group
        if group1 in antonyms and antonyms[group1] != group2:
            antonym_group = antonyms[group1]
            group2 = make_synonyms(synonyms, antonyms, groups, group2, antonym_group)
        if group2 in antonyms and antonyms[group2] != group1:
            antonym_group = antonyms[group2]
            make_synonyms(synonyms, antonyms, groups, group1, antonym_group)
    return current_group


def make_relations(relation_no):
    synonyms = dict()
    antonyms = dict()
    groups = dict()
    current_group = 0
    for relation in range(relation_no):
        (relation, word1, word2) = input().split()
        current_relation = get_relation(synonyms, antonyms, word1, word2)
        if current_relation == '2' and relation == '1':
            print('NO')
            continue
        if current_relation == '1' and relation == '2':
            print('NO')
            continue
        print('YES')
        current_group = make_relation(synonyms, antonyms, groups, word1, word2, relation, current_group)
    return (synonyms, antonyms)


def answer_questions(question_no, synonyms, antonyms):
    for question in range(question_no):
        (word1, word2) = input().split()
        print(get_relation(synonyms, antonyms, word1, word2))


def main():
    (word_no, relation_no, question_no) = [int(number) for number in input().split()]
    input()
    (synonyms, antonyms) = make_relations(relation_no)
    answer_questions(question_no, synonyms, antonyms)


main()
