vowels = 'aeiouy'
n = int(input())
p = [int(x) for x in input().split()]
for i in range(n):
    s = input()
    vowelsCnt = 0
    for c in s:
        if c in vowels:
            vowelsCnt += 1
    if vowelsCnt != p[i]:
        print('NO')
        break
else:
    print('YES')

