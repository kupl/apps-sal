T = int(input())
n = list(map(int, input().split()))

for i in n:
    l1 = [1]
    l2 = [2]
    l3 = [4]
    l4 = [3]
    for t in range(1, i):
        l1.append(l1[-1] + 3*2**(t-1))
        l2.append(l1[-1] + 1)
        l3.append(l3[-1] + 6*2**(t-1))
        l4.append(l4[-1]*2)
    l1 = list(map(str, l1))
    l2 = list(map(str, l2))
    l3 = list(map(str, l3))
    l4 = list(map(str, l4))
        
    print(' '.join(l1))
    print(' '.join(l2))
    print(' '.join(l3))
    print(' '.join(l4))
