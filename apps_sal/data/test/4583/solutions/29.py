A = list(map(int, list(input())))

def sign(x):
    return "+" if x == 1 else "-"
for i in [1,-1]:
    for j in [1,-1]:
        for k in [1,-1]:
            if A[0] + A[1] * i + A[2] * j + A[3] * k == 7:
                print(str(A[0]) + sign(i) + str(A[1]) + sign(j) +str(A[2]) + sign(k) + str(A[3]) + "=7")
                return
