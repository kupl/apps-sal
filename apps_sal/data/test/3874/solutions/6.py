__author__ = 'Think'


def check(s, password):
    if len(s) != len(password):
        return False
    for i in range(len(password)):
        if password[i] != '?':
            if password[i] != s[i]:
                return False
    return True


(n, m) = [int(i) for i in input().split()]
filenames = []
for i in range(n):
    filenames.append(input())
deleted_indices = [int(i) - 1 for i in input().split()]
deleted = []
fails = False
for i in deleted_indices:
    deleted.append(filenames[i])
length = len(deleted[0])
for s in deleted[1:]:
    if len(s) != length:
        fails = True
        print('No')
        break
if not fails:
    answer = list(deleted[0])
    for i in range(length):
        for s in deleted[1:]:
            if s[i] != answer[i]:
                answer[i] = '?'
                break
    for index in range(n):
        if index not in deleted_indices:
            if check(filenames[index], answer):
                print('No')
                fails = True
                break
    if not fails:
        print('Yes')
        for s in answer:
            print(s, end='')
        print()
