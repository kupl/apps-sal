N = int(input())
S, T = input().split()

new_string = ""

for i in range(0, N):
    ST_string = S[i] + T[i]
    new_string += ST_string

print(new_string)
