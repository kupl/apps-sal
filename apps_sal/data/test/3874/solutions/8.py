n = int(input().split()[0])

all_files = [str(input()) for i in range(n)]

index_to_del = [int(i) - 1 for i in (input().split())]


def find_pattern(all_files, index_to_del):
    for i in index_to_del[1:]:
        if len(all_files[i]) != len(all_files[index_to_del[0]]):

            return "No"
    pattern = ''
    for i in range(len(all_files[index_to_del[0]])):
        added = False
        for j in (index_to_del[1:]):
            if all_files[j][i] != all_files[index_to_del[0]][i]:
                if not added:
                    pattern += '?'
                    added = True
        if not added:
            pattern += all_files[index_to_del[0]][i]

    for i in range(len(all_files)):
        if i not in index_to_del:
            if len(all_files[i]) == len(pattern):
                matching_chars = []
                for index in range(len(pattern)):
                    matching_chars.append(all_files[i][index] == pattern[index] or pattern[index] == '?')
                if all(matching_chars):
                    return "No"

    print("Yes")
    return pattern


print(find_pattern(all_files, index_to_del))
