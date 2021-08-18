s = input()

o = -1

sol = []

p = True

for i in range(0, len(s)):

    if s[i] == '0':

        if o == -1:

            sol.append([i + 1])

        else:

            sol[o].append(i + 1)

            o -= 1

    else:

        o += 1

        if o == len(sol):

            p = False

            break

        else:

            sol[o].append(i + 1)

if p == False or o != -1:

    print("-1")

else:

    print(len(sol))

    print("\n".join([str(len(sub)) + " " + " ".join(map(str, sub)) for sub in sol]))
