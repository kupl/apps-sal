a = int(input())
l = sorted(set(map(int, input().split())))
for i in range(len(l) - 2):
    if l[i] + 2 == l[i + 2]:
        print('YES')
        break
else:
    print("NO")
