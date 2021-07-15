from collections import Counter
n = int(input())
s = input()
c = Counter(s)
if n & 1 or c['('] > (n // 2) or c[')'] > (n // 2):
    print(":(")
else:
    f1 = n // 2 - c['(']
    f2 = n // 2 - c[')']
    r = []
    for v in s:
        if v == "?":
            if f1 > 0:
                r.append("(")
                f1 -= 1
            else:    
                r.append(")")
                f2 -= 1
        else:
            r.append(v)
    cnt = 0        
    for i, v in enumerate(r):
        if v == "(":
            cnt += 1
        else:    
            cnt -= 1
        if i < n-1 and cnt <= 0:
            print(":(")
            break
    else:
        print("".join(r))


