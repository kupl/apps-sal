def main():
    N = int(input())
    tasks = []
    for i in range(N):
        (A, B) = [int(x) for x in input().split(' ')]
        tasks.append({'time': A, 'deadline': B})
    tasks.sort(key=lambda task: task['deadline'])
    tot = 0
    in_time = 'Yes'
    for i in range(len(tasks)):
        t = tasks[i]['time']
        d = tasks[i]['deadline']
        tot += t
        if tot > d:
            in_time = 'No'
            break
    print(in_time)


main()
