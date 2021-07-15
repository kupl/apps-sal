def go():
    n = int(input())
    s = [i for i in input()]
    for i in range(1, n + 1):
        if n % i == 0:
            s[0:i] = s[0:i][::-1]
    return ''.join(s)
print(go())

