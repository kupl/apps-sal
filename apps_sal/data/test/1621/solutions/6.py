s = input()
k = int(input())
w = list(map(int, input().split()))
c = chr(w.index(max(w)) + ord('a'))


def f(s):
    result = 0
    for i in range(len(s)):
        result += w[ord(s[i]) - ord('a')] * (i + 1)
    return result


print(f(s + c * k))
