N = int(input())
S, T = input().split()
def new():
    text = []
    for i in range(N):
        text.append(S[i])
        text.append(T[i])
    return "".join(text)
print(new())
