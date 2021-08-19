with open(0) as f:
    (N, A, B, *H) = map(int, f.read().split())
diff = A - B
T = (max(H) + B - 1) // B


def clearable(t):
    Higher = [h - B * t for h in H if h - B * t > 0]
    return True if sum([(h + diff - 1) // diff for h in Higher]) <= t else False


def binary_search(a, b, judge):
    if a == b:
        return (a, b)
    c = a + (b - a) // 2
    return (a, c) if judge(c) else (c + 1, b)


(a, b) = (0, T)
while a != b:
    (a, b) = binary_search(a, b, clearable)
print(a)
