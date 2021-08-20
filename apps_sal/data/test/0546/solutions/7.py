import sys
good_letters = set(input())
pattern = input()
input()
for line in sys.stdin:
    query = line.strip()
    diff = len(query) - len(pattern) + 1
    if diff < 0:
        print('NO')
        continue
    query_index = 0
    pattern_index = 0
    question = None
    result = 'NO'
    while pattern_index < len(pattern) and query_index < len(query):
        current_letter = query[query_index]
        current_pattern = pattern[pattern_index]
        if current_pattern == '*':
            if diff == 0:
                pattern_index += 1
            elif current_letter in good_letters:
                break
            else:
                query_index += 1
                diff -= 1
        elif current_pattern == '?':
            if current_letter in good_letters:
                query_index += 1
                pattern_index += 1
            else:
                break
        elif current_letter != current_pattern:
            break
        else:
            query_index += 1
            pattern_index += 1
    if query_index == len(query) and pattern_index == len(pattern) - 1 and (pattern[pattern_index] == '*'):
        result = 'YES'
    if query_index == len(query) and pattern_index == len(pattern):
        result = 'YES'
    print(result)
