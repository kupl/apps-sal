(A, B, C) = map(int, input().split())
a = b = c = False
odd = 0
if A % 2:
    odd += 1
    a = True
if B % 2:
    odd += 1
    b = True
if C % 2:
    odd += 1
    c = True
result = 0
if odd == 1:
    if a:
        B = B + 1
        C = C + 1
        result += 1
    elif b:
        A = A + 1
        C = C + 1
        result += 1
    elif c:
        A = A + 1
        B = B + 1
        result += 1
if odd == 2:
    if a & b:
        A = A + 1
        B = B + 1
        result += 1
    elif b & c:
        B = B + 1
        C = C + 1
        result += 1
    elif a & c:
        A = A + 1
        C = C + 1
        result += 1
result += int((3 * max(A, B, C) - A - B - C) / 2)
print(result)
