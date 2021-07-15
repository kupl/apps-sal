t = int(input())
for _ in range(t):
    n = int(input())
    A = map(int, input().split())
    B = map(int, input().split())
    
    seen_pos = seen_neg = False
    for a, b in zip(A, B):
        if (b > a and not seen_pos) or (b < a and not seen_neg):
            print('NO')
            break
        
        if a > 0:
            seen_pos = True
        elif a < 0:
            seen_neg = True        
    else:
        print('YES')
