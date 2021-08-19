S = str(input())

abs_list = []

for i in range(1, len(S) - 1):
    # print(S[i-1:i+2])
    X = int(S[i - 1:i + 2])
    abs_list.append(abs(X - 753))
    abs_min = min(abs_list)

print(abs_min)
