A = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
Z = [0] * 64
for i in range(64):
    r = 0
    for j in range(64):
        for k in range(64):
            if i == (j & k):
                r += 1
    Z[i] = r
    #print(str(i) + ".", A[i], "=>", r)

r = 1
for c in input():
    #print("c:", c, "idx:", A.index(c), "z:", Z[A.index(c)])
    r = (r * Z[A.index(c)]) % 1000000007
print(r)

"""
V_V & V_V = V_V

__V & V_V = V_V
V_V & __V = V_V

V__ & V_V = V_V
V_V & V__ = V_V

___ & V_V = V_V
V_V & ___ = V_V

__V & V__ = V_V
V__ & __V = V_V
"""
