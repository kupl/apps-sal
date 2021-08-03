from collections import Counter

T = int(input())
N = []
case = []
for _ in range(T):
    N.append(int(input()))
    case.append(list(map(int, input().split())))

for t in range(T):
    if N[t] % 2 == 1:
        print('Second')
    else:
        count = Counter(case[t])
        if all([i % 2 == 0 for i in list(count.values())]):
            print('Second')
        else:
            print('First')
