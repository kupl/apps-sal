N = int(input())

w = list(map(int, input().split(' ')))
key = [i + 1 for i in range(N)]

w_dict = dict(zip(key, w))

w_dict = sorted(w_dict.items(), key=lambda x: x[1])

number = [row[0] for row in w_dict]

passenger = input()
ans = []
gaikouteki = []
now = 0
for i in passenger:
    if i == '0':
        ans.append(number[now])
        gaikouteki.append(number[now])
        now += 1
    else:
        ans.append(gaikouteki[-1])
        gaikouteki.pop()
print(' '.join(map(str, ans)))
