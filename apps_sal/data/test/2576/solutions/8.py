# map(int, input().split())
def main():
    a, b, c, d = map(int, input().split())
    f = []
    f += [a + b] * 100
    f += [c + d] * 100
    f.sort()
    print(f[100])


rw = int(input())
for wewq in range(rw):
    main()
