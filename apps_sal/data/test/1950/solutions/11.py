import heapq
n = input()
A = list(map(int, input().split())) 
if (len(A) % 2 == 0):
    A.append(0)
st = 0
heapq.heapify(A)
while (len(A) > 1):
    abc = 0
    a = heapq.heappop(A) # Удаляет и возвращает наименьший элемент кучи A
    b = heapq.heappop(A)
    c = heapq.heappop(A)
    abc = a + b + c
    st = st + abc
    heapq.heappush(A, abc) #Добавляет значение объекта abc в кучу A
print(st)

