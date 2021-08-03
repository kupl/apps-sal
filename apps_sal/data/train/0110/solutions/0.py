for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))

    peaks = [0 for i in range(n)]
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks[i] = 1

    cnt = 0
    max_peaks = 0
    answer = 0

    for i in range(k - 1):
        cnt += peaks[i]
        max_peaks += peaks[i]

    for i in range(k - 1, n - 1):
        cnt -= peaks[i - k + 2]
        cnt += peaks[i]
        if cnt > max_peaks:
            max_peaks = cnt
            answer = i - k + 2

    print(max_peaks + 1, answer + 1)
