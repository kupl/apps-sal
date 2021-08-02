# 割り切る数は、Aの総和の約数である
# 約数について大きい順にすべて試して、当てはまるものがあれば答え

# 8,20を7の倍数に近づけるとき、
# 8 -> mod 7が1であり、-1か+6で7の倍数になる
# 20 -> mod 7が6であり、-6か+1で7の倍数になる
# 負の和と正の和が一致したとき、そのときの絶対値が答え
# 1,1,2,3,4,5と並べて、前から足していくのが最善。入れ替えると絶対値が増加するので損しかしない

import sys
readline = sys.stdin.readline

N, K = list(map(int, readline().split()))
A = list(map(int, readline().split()))

all = sum(A)
divisors = []
for i in range(1, int(all ** 0.5) + 1):
    if all % i == 0:
        divisors.append(i)
        divisors.append(all // i)

divisors = sorted(divisors, reverse=True)

for d in divisors:
    mods = [0] * (N)
    for i in range(len(A)):
        mods[i] = A[i] % d
    mods = sorted(mods)
    mods_front = [0] * N
    mods_front[0] = mods[0]
    for i in range(1, N):
        mods_front[i] = mods_front[i - 1] + mods[i]
    mods_back = [0] * N
    mods_back[-1] = d - mods[-1]
    for i in range(N - 2, -1, -1):
        mods_back[i] = mods_back[i + 1] + (d - mods[i])
    for i in range(N - 1):
        if mods_front[i] == mods_back[i + 1]:
            if K >= mods_front[i]:
                print(d)
                return
else:
    print((1))
