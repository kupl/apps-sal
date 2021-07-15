N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

def binary1(L, R, list_, threshold):
    while L + 1 < R:
        x = (L + R)//2
        if list_[x] < threshold:
            L = x            
        else:
            R = x
    return L

def binary2(L, R, list_, threshold):
    while L + 1 < R:
        x = (L + R)//2
        if list_[x] > threshold:
            R = x            
        else:
            L = x
    return L

ans = []
for b in B:
    L = -1
    R = N
    a = binary1(L, R, A, b) + 1
    c = N - binary2(L, R, C, b) - 1
    ans.append(a*c)
print((sum(ans)))

