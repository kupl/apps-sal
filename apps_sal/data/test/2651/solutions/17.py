# solution
import io


def data(): return list(map(int, input().split()))


data()
def q(x): return sum(j * (len(x) - 1 - 2 * i)for i, j in enumerate(x))


print(q(data()) * q(data()) % (10**9 + 7))
