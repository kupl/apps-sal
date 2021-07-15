k = int(input())

def cal(k):
    n = 7
    for i in range(1,10000000):
        if n % k == 0:
            return i
        else:
            n = (n *10 + 7) % k
    return -1

print(cal(k))
