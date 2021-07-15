
def main():
    n, m, k = [int(a) for a in input().split()]
    bis = [int(a) for a in input().split()]
    total_length = bis[-1] - bis[0]
    between = []
    for i in range(len(bis) - 1):
        between.append(bis[i+1] - bis[i])
    between.sort(reverse=True)
    for i in range(k-1):
        total_length -= between[i]
    total_length += k
    print(total_length)
main()

