N = int(input())
S = list(map(str, input().split()))

if len(set(S)) == 3:
    print("Three")
elif len(set(S)) == 4:
    print("Four")
