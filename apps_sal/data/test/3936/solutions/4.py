class modint:
    mod = 0
    has_been_set = False

    def __init__(self, v=0, m=None):
        if m != None:
            assert m >= 1
            assert not modint.has_been_set
            modint.mod = m
            modint.has_been_set = True
        assert modint.has_been_set
        self._v = v if 0 <= v < modint.mod else v % modint.mod

    def __add__(self, other):
        if isinstance(other, modint):
            res = self._v + other._v
            if res > modint.mod:
                res -= modint.mod
        else:
            res = self._v + other
        return modint(res)

    def __sub__(self, other):
        if isinstance(other, modint):
            res = self._v - other._v
            if res < 0:
                res += modint.mod
        else:
            res = self._v - other
        return modint(res)

    def __mul__(self, other):
        if isinstance(other, modint):
            return modint(self._v * other._v)
        else:
            return modint(self._v * other)

    def __floordiv__(self, other):
        if isinstance(other, modint):
            other = other._v
        inv = pow(other, -1, modint.mod)
        return modint(self._v * inv)

    def __pow__(self, other):
        assert isinstance(other, int) and other >= 0
        return modint(pow(self._v, other, modint.mod))

    def __radd__(self, other):
        return modint(self._v + other)

    def __rsub__(self, other):
        return modint(other - self._v)

    def __rmul__(self, other):
        return modint(self._v * other)

    def __rfloordiv__(self, other):
        inv = pow(self._v, -1, modint.mod)
        return modint(other * inv)

    def __iadd__(self, other):
        if isinstance(other, modint):
            self._v += other._v
            if self._v >= modint.mod:
                self._v -= modint.mod
        else:
            self._v += other
            if self._v < 0 or self._v >= modint.mod:
                self._v %= modint.mod
        return self

    def __isub__(self, other):
        if isinstance(other, modint):
            self._v -= other._v
            if self._v < 0:
                self._v += modint.mod
        else:
            self._v -= other
            if self._v < 0 or self._v >= modint.mod:
                self._v %= modint.mod
        return self

    def __imul__(self, other):
        if isinstance(other, modint):
            self._v *= other._v
        else:
            self._v *= other
        if self._v < 0 or self._v >= modint.mod:
            self._v %= modint.mod
        return self

    def __ifloordiv__(self, other):
        if isinstance(other, modint):
            other = other._v
        inv = pow(other, -1, modint.mod)
        self._v *= inv
        if self._v > modint.mod:
            self._v %= modint.mod
        return self

    def __ipow__(self, other):
        assert isinstance(other, int) and other >= 0
        self._v = pow(self._v, other, modint.mod)
        return self

    def __eq__(self, other):
        if isinstance(other, modint):
            return self._v == other._v
        else:
            if other < 0 or other >= modint.mod:
                other %= modint.mod
            return self._v == other

    def __ne__(self, other):
        if isinstance(other, modint):
            return self._v != other._v
        else:
            if other < 0 or other >= modint.mod:
                other %= modint.mod
            return self._v != other

    def __str__(self):
        return str(self._v)

    def __repr__(self):
        return str(self._v)

    def __int__(self):
        return self._v


n = int(input())
s = input()
t = input()
mod = 10**9 + 7
ans = modint(0, m=mod)
if s[0] == t[0]:
    ans += 3
    i = 1
else:
    ans += 6
    i = 2
while i < n:
    if s[i - 1] != t[i - 1] and s[i] == t[i]:
        ans *= 1
    elif s[i] == t[i]:
        ans *= 2
    elif s[i - 1] != t[i - 1]:
        ans *= 3
        i += 1
    else:
        ans *= 2
        i += 1
    i += 1
print(ans)
