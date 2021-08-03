n = int(input())
s = input()
if n % 4 != 0:
    print("===")
else:
    A = s.count("A")
    C = s.count("C")
    G = s.count("G")
    T = s.count("T")
    Q = s.count("?")
    #print(A, C, G, T, Q)
    # print(l)
    if max((A, C, G, T)) <= n // 4:
        ns = ""
        for i in range(n):
            if s[i] == '?':
                if n // 4 - A > 0:
                    ns += "A"
                    A += 1
                elif n // 4 - C > 0:
                    ns += "C"
                    C += 1
                elif n // 4 - G > 0:
                    ns += "G"
                    G += 1
                elif n // 4 - T > 0:
                    ns += "T"
                    T += 1
            else:
                ns += s[i]
        if "?" in ns:
            print("===")
        else:
            print(ns)
    else:
        print("===")
