S = input()
mod = 10**9 + 7
La, Lq, Rc, Rq = 0, 0, S.count("C"), S.count("?")
ans = 0
def f(x, y): return pow(x, y, mod) if y >= 0 else 0


for s in S:
    Rc -= s == "C"
    Rq -= s == "?"
    if s == "B" or s == "?":
        ans += (La * f(3, Lq) + Lq * f(3, Lq - 1)) * (Rc * f(3, Rq) + Rq * f(3, Rq - 1))
        ans %= mod
    La += s == "A"
    Lq += s == "?"
print(ans)
