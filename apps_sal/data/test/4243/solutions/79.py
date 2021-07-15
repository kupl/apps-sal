x = int(input())

g500 = x // 500
g5 = (x-g500*500)//5

print(g500 *1000 + g5 * 5)
