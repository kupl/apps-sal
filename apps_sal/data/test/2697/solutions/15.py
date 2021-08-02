def prime_eratosthenes(n):
    prime_list = []
    z = []
    for i in range(2, n + 1):
        if i not in prime_list:
            # print(i)
            z.append(i)
            for j in range(i * i, n + 1, i):
                prime_list.append(j)
    print(len(z))

    # print(prime_list)
x = int(input())
prime_eratosthenes(x);
