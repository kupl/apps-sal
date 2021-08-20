def R():
    return map(int, input().split())


(n, m, a, b) = R()
t = list(R())
print('Incorrect' if n - m == 1 and min(t) != a and (max(t) != b) or min(t) < a or max(t) > b else 'Correct')
