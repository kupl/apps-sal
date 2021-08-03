N_M = list(map(int, input().split()))
Weights = list(map(int, input().split()))
Good_Books = list(map(int, input().split()))
Times = []
Count = sum(N_M)
for I in range(N_M[0]):
    try:
        Count = Good_Books.index(I + 1)
    except ValueError:
        pass
    if not Count == sum(N_M):
        Times.append([Count, I])
    Count = sum(N_M)
Times.sort()
Times = list(Times)
Heap = []
for I in range(len(Times)):
    Heap.append(Times[I][1])
Count = 0
Positions = sum(N_M)
for I in range(N_M[1]):
    Positions = Heap.index(Good_Books[I] - 1)
    for I_2 in range(Positions):
        Count += Weights[Heap[I_2]]
    Heap = [Heap[Positions]] + Heap[:Positions] + Heap[Positions + 1:]
print(Count)
