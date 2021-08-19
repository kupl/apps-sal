while True:
    try:
        caption = input().split()
        n = int(caption[0])
        servers = [i for i in range(1, n + 1)]
        answer = []
        q = int(caption[1])
        using = {}
        for i in range(q):
            tasks = input().split()
            time = int(tasks[0])
            key = int(tasks[0]) + int(tasks[2])
            for i in list(using.keys()):
                if time >= i:
                    servers += using[i]
                    servers.sort()
                    del using[i]
            need = int(tasks[1])
            touse = len(servers)
            if need > touse:
                answer.append(-1)
            else:
                amount = servers[:need]
                servers = servers[need:]
                sums = sum(amount)
                if not using.get(key):
                    using[key] = amount
                else:
                    using[key] += amount
                answer.append(sums)
        for i in answer:
            print(i)
    except EOFError:
        break
