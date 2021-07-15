class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_dic = {}
        power_dic_sub = {}
        for i in range(lo, hi+1):
            power_dic_sub[i] = self.getPower(i, 0, [], power_dic)
        result_tmp = sorted(power_dic_sub.items(), key=lambda kv: kv[1], reverse= False)
        return result_tmp[k - 1][0]

    def getPower(self, num, power,power_record, power_dic):
        if num == 1:
            for i in power_record:
                if not power_dic[i]:
                    power_dic[i] = power - power_record.index(i)
            return power
        if num in power_dic:
            return power_dic[num]
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num +1
        power += 1
        return self.getPower(num, power, power_record, power_dic)
