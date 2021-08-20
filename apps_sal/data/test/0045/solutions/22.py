str_params = input()
[n, k] = [int(s) for s in str_params.split(' ')]
parts = (1 + k) / 2 * k
if parts <= n:
    nod = n / parts
    while (nod % 1 != 0) | (parts % 1 != 0):
        if nod < parts:
            if nod % 1 != 0:
                nod = int(nod)
            else:
                nod = nod - 1
            parts = n / nod
        else:
            if parts % 1 != 0:
                parts = int(parts) + 1
            else:
                parts = parts + 1
            nod = n / parts
    numbers = [nod * (x + 1) for x in range(k)]
    numbers[k - 1] = n - (1 + k - 1) / 2 * (k - 1) * nod
    if numbers[0] == 0:
        print(-1)
    else:
        print(' '.join(map(str, list(map(int, numbers)))))
else:
    print(-1)
"while (sum(numbers)<n):\n\t\n\n\t33/5 = 6.6\n\t33/11 = 3\n\t\n\t33/6 = 5.5\n\t\n\t24/10 = 2.4\n\t\n\t\n\t\ni = 1\nwhile (sum(numbers)<n) & (i<k):\n\twhile sum(numbers)<n:\n\t\tnumbers = [numbers[x]*i for x in range(k)]\n\t\tprint (i, numbers)\n\t\ti = i+1\nprint (numbers)\nif sum(numbers)>n:\n\tprint (-1)\nif sum(numbers)==n:\n\tprint (' '.join(map(str,numbers)))"
