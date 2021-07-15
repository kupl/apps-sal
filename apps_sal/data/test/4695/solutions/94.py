'''
abc062 A - Grouping
https://atcoder.jp/contests/abc062/tasks/abc062_a
'''

dirs = [{1, 3, 5, 7, 8, 10, 12}, {4, 6, 9, 11}, {2}]

i = list(map(int, input().split()))

for dir in dirs:
    if i[0] in dir and i[1] in dir:
        print('Yes')
        return
else:
    print('No')

