n = int(input())
for i in range(n):
    s = list([ord(x) for x in list(input())])
    if sorted(s) == list(range(min(s), max(s) + 1)):
        print('Yes')
    else:
        print('No')
