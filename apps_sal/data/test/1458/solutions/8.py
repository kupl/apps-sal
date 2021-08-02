N = int(input())
S = input()


def stoi(s):
    return ord(s) - 97


for i in range(N - 1):
    if stoi(S[i]) > stoi(S[i + 1]):
        print("YES")
        print(i + 1, i + 2)
        break
else:
    print("NO")
