(N, K) = list(map(int, input().split()))
string = input()
for _ in range(K):
    (fr, to, c1, c2) = input().split()
    (fr, to) = (int(fr), int(to))
    (fr, to) = (fr - 1, to - 1)
    for i in range(fr, to + 1):
        if string[i] == c1:
            string = string[:i] + c2 + string[i + 1:]
print(string)
