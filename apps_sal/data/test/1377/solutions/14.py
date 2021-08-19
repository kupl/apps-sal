n = int(input())
li = list(map(int, input().split()))
x = li.index(max(li))
if li[:x] == sorted(li[:x]) and li[x:] == sorted(li[x:])[::-1]:
    print('YES')
else:
    print('NO')
