class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        items = []
        for i in range(len(values)):
            items.append((values[i], labels[i]))

        items.sort(key=lambda item: item[0], reverse=True)
        dic = Counter(labels)

        for item in dic:
            if dic[item] > use_limit:
                dic[item] = use_limit

        largest = 0
        print(dic)
        print(items)
        for num in items:
            if num_wanted == 0:
                break
            current_label = num[1]
            value = num[0]
            print(current_label)

            if dic[current_label] > 0:
                num_wanted -= 1
                dic[current_label] -= 1
                largest += value
        return largest
