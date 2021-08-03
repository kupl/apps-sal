a = int(input())
for i in range(a):
    x, y = list(map(int, input().split()))
    ans = []
    for i in range(x):
        s = input()
        ans.append(s[-1])

    print(s.count('D') + ans.count('R'))
