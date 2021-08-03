S = list(input())
T = list(input())
print("Yes" if len(set(S)) == len(set(T)) == len(set(zip(S, T))) else "No")
