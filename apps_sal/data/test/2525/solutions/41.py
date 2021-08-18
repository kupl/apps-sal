

s = input()
q = int(input())

inv = False

fro = ""
end = ""

for _ in range(q):
    query = list(map(str, input().split()))

    if query[0] == "1":
        inv = not inv

    else:
        t = int(query[1])
        instr = query[2]
        if not inv:
            if t == 1:
                fro = instr + fro
            else:
                end = end + instr

        else:
            if t == 1:
                end = end + instr[::-1]
            else:
                fro = instr[::-1] + fro

ans = fro + s + end

if not inv:
    print(ans)

else:
    print(ans[::-1])
