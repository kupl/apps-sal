N = int(input())
S = input()


def s():
    name = 'No'
    if S[0:int(N / 2)] == S[int(N / 2):]:
        name = 'Yes'
    return name


print(s())
