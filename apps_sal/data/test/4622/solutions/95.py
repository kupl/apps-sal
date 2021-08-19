from collections import Counter
cnt = input()
num_list = Counter(map(int, input().split()))
for _ in num_list.values():
    if _ > 1:
        print('NO')
        break
else:
    print('YES')
