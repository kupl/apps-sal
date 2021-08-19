class Solution:
    def clumsy(self, N: int) -> int:
        numbers = list(range(N + 1))[1:]
        numbers.reverse()
        inter_results = []
        for idx, v in enumerate(numbers):
            if idx % 4 == 0:
                inter_results.append(v)
            elif idx % 4 == 1:
                inter_results[-1] *= v
            elif idx % 4 == 2:
                inter_results[-1] = int(inter_results[-1] / v)
            elif idx % 4 == 3:
                inter_results.append(v)
        # print(inter_results)
        final_results = 0
        for idx, v in enumerate(inter_results):
            if idx == 0:
                final_results += v
            elif idx % 2 == 1:
                final_results += v
            elif idx % 2 == 0:
                final_results -= v
        return final_results
