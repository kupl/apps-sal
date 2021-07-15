t = int(input())

for _ in range(t):
    n = int(input())
    s = [int(x) for x in input()]
    A = s[0::2] 
    B = s[1::2] 
    if n%2 == 0:
        if any(x%2 == 0 for x in B):
            print(2)
        else:
            print(1)
    else:
        if any(x%2 == 1 for x in A):
            print(1)
        else:
            print(2)



